import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api";
import "../styles/Login.css";

export default function Login() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [erro, setErro] = useState("");
  const navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();
    setErro("");
    const data = await login(email, senha);
    console.log("RESPOSTA LOGIN:", data);

    if (data.erro) {
      setErro(data.erro);
      return;
    }

    localStorage.setItem("usuario", data.usuario);
    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);

    navigate("/home");
  }

  return (
   <div className="login-container">
    <h2>Login</h2>
    {erro && <p style={{ color: "red" }}>{erro}</p>}

    <form onSubmit={handleLogin}>
        <input
        type="email"
        placeholder="email"
        className="login-input"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        />

        <input
        type="password"
        placeholder="senha"
        className="login-input"
        value={senha}
        onChange={(e) => setSenha(e.target.value)}
        />

        <button className="login-button" type="submit">
        Entrar
        </button>
    </form>
    </div>

  );
}
