import Navbar from "../components/Navbar";
import "../styles/Home.css";

export default function Home() {
  return (
   <div>
   <Navbar />
    <div className="page-container">
    <h2 className="page-title">Interface Principal</h2>
    <p>Escolha uma das opções acima para navegar.</p>
    </div>
    </div>

  );
}
