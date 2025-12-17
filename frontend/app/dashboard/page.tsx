'use client';
import { useEffect, useState } from 'react';
import axios from 'axios';
import MatchCard from '../../components/MatchCard';

export default function Dashboard() {
  const [data, setData] = useState({ fixtures: [], value_bets: [] });

  useEffect(() => {
    axios.get('/api/matches/daily').then(res => setData(res.data));
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-2xl">Jogos do Dia</h2>
      <div className="grid grid-cols-3 gap-4">
        {data.fixtures.map(f => <MatchCard key={f.id} match={f} isValue={data.value_bets.includes(f.id)} />)}
      </div>
    </div>
  );
}