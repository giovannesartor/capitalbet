import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="bg-gray-800 p-4">
      <ul className="flex space-x-4">
        <li><Link href="/dashboard">Dashboard</Link></li>
        <li><Link href="/matches">Comparador Odds</Link></li>
        <li><Link href="/simulator">Simulador</Link></li>
        <li><Link href="/chat">Assistente</Link></li>
      </ul>
    </nav>
  );
}