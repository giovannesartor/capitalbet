import { BarChart, PieChart, LineChart } from 'recharts';

export default function Charts({ data }) {
  // Example
  return (
    <>
      <BarChart data={data.form} /> {/* Forma recente */}
      <PieChart data={data.goals} /> {/* % Over 2.5 */}
      <LineChart data={data.balanceHistory} /> {/* For simulator */}
    </>
  );
}