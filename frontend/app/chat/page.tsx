'use client';
import { useState } from 'react';
import axios from 'axios';

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const send = async () => {
    setMessages([...messages, { user: input }]);
    const res = await axios.post('/api/chat', { message: input });
    setMessages([...messages, { bot: res.data.response }]);
    setInput('');
  };

  return (
    <div className="chat-window">
      {messages.map((m, i) => <div key={i}>{m.user || m.bot}</div>)}
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={send}>Enviar</button>
    </div>
  );
}