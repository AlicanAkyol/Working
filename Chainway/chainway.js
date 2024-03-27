const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const port = 3001;

app.use(bodyParser.json());

const RPC_URL = "https://svc.blockdaemon.com/bitcoin/mainnet/native";
const CAPIKEYT = "zpka_a4f0aff81df04442a8facebbe46690e9_3796406a";
const confirmationsThreshold = 6;
const trackedTransactions = new Set();
const finalizedTransactionsQueue = [];

const authHeaders = {
  headers: {
    Authorization: `Bearer ${CAPIKEYT}`,
    "Content-Type": "application/json",
  },
};

async function checkForFinalizedTransactions() {
  for (const txid of trackedTransactions) {
    try {
      const response = await axios.post(
        `${RPC_URL}/gettransaction`,
        { txid },
        authHeaders
      );
      const { confirmations, blockhash } = response.data;

      if (confirmations >= confirmationsThreshold) {
        finalizedTransactionsQueue.push(
          `Transaction with txid ${txid} finalized at block with hash ${blockhash}`
        );
        trackedTransactions.delete(txid);
      }
    } catch (error) {
      console.error(`Error checking transaction ${txid}: ${error.message}`);
    }
  }
}

setInterval(checkForFinalizedTransactions, 500);

app.post("/new-tx", (req, res) => {
  const { txid } = req.body;
  if (!txid) {
    return res.status(400).json({ error: "Missing 'txid' parameter" });
  }

  trackedTransactions.add(txid);

  setTimeout(() => {
    const finalized = finalizedTransactionsQueue.splice(
      0,
      finalizedTransactionsQueue.length
    );
    res.json(finalized);
  }, 1000);
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
