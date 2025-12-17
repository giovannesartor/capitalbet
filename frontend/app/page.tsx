import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Navbar />
      <main className="p-8">
        <h1 className="text-4xl font-bold">Bem-vindo ao Capital Bet</h1>
        <Link href="/dashboard">Ir para Dashboard</Link>
      </main>
      <footer className="fixed bottom-0 w-full p-4 bg-gray-800 text-center">
        Capital Bet é uma plataforma de análise esportiva e simulação. Não realizamos apostas reais nem operamos como casa de apostas.
      </footer>
    </div>
  );
}