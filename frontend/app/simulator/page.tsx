'use client';
import { useState } from 'react';
import axios from 'axios';
import Charts from '../../components/Charts';

export default function Simulator() {
  const [history, setHistory] = useState([]);
  const [balance, setBalance] = useState(1000);

  // Fetch history, place bet via API
  return (
    <div>
      <h2>Saldo: {balance}</h2>
      {/* Form to simulate bet */}
      <Charts data={history} /> {/* Line chart for balance growth */}
    </div>
  );
}