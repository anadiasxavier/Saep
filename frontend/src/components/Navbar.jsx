import { useNavigate } from "react-router-dom";
import "../styles/Navbar.css";

export default function Navbar() {
  const navigate = useNavigate();
  const usuario = localStorage.getItem("usuario");

  function logout() {
    localStorage.clear();
    navigate("/");
  }

  return (
   <div className="navbar-container">
    <p className="navbar-user">Usuário: {usuario}</p>

    <div className="navbar-buttons">
        <button className="navbar-button" onClick={() => navigate("/home")}>
        Home
        </button>
        <button className="navbar-button" onClick={() => navigate("/produtos")}>
        Produtos
        </button>
        <button className="navbar-button" onClick={() => navigate("/estoque")}>
        Estoque
        </button>
        <button className="navbar-button" onClick={logout}>
        Logout
        </button>
    </div>
    </div>

  );
}
