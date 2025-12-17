import Link from 'next/link';

export default function MatchCard({ match, isValue }) {
  return (
    <div className="card bg-gray-800 p-4 shadow-md rounded-lg fade-in">
      <h3>{match.home} vs {match.away}</h3>
      <p>Liga: {match.league}</p>
      <p>Horário: {match.time}</p>
      <p>Odds: 1 - {match.odds.home}, X - {match.odds.draw}, 2 - {match.odds.away}</p>
      <p>Prob: {match.prob}%</p>
      {isValue && <span className="badge bg-positive">🔥 VALUE BET</span>}
      <Link href={`/stats/${match.id}`}>Estatísticas</Link>
      <button>Simular Aposta</button>
    </div>
  );
}