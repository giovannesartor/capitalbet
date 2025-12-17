'use client';
import { useParams } from 'next/navigation';
import Charts from '../../../components/Charts';
import axios from 'axios';
import { useEffect, useState } from 'react';

export default function Stats() {
  const { id } = useParams();
  const [stats, setStats] = useState({});

  useEffect(() => {
    axios.get(`/api/stats/${id}`).then(res => setStats(res.data));
  }, [id]);

  return (
    <div className="p-8">
      <ul className="tabs"> {/* Use tabs for Visão Geral, Estatísticas, H2H */} </ul>
      <Charts data={stats} /> {/* Bars, donuts, etc. */}
    </div>
  );
}