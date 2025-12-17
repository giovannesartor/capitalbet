export default function OddsTable({ data }) {
  return (
    <table className="w-full">
      <thead>
        <tr><th>Mercado</th><th>Melhor Odd</th></tr>
      </thead>
      <tbody>
        {Object.entries(data).map(([market, best]) => (
          <tr key={market}><td>{market}</td><td className="text-positive">{best}</td></tr>
        ))}
      </tbody>
    </table>
  );
}