import { useState, useEffect } from "react";
import { getProdutos, movimentarEstoque } from "../api";
import Navbar from "../components/Navbar";
import "../styles/Estoque.css";

export default function Estoque() {
  const [produtos, setProdutos] = useState([]);
  const [produtoId, setProdutoId] = useState("");
  const [tipo, setTipo] = useState("entrada");
  const [quantidade, setQuantidade] = useState("");
  const [dataMov, setDataMov] = useState("");

  useEffect(() => {
    async function carregar() {
      const data = await getProdutos();
      const produtos = Array.isArray(data.results) ? data.results : [];
      produtos.sort((a, b) => a.nome.localeCompare(b.nome));
      setProdutos(produtos);
    }
    carregar();
  }, []);

  async function enviar() {
    if (!produtoId || !quantidade || !dataMov) {
      alert("Preencha todos os campos!");
      return;
    }

    const res = await movimentarEstoque({
      produto: produtoId,
      tipo,
      quantidade,
      data: dataMov,
    });

    if (res.alerta) {
      alert("Estoque abaixo do mínimo!");
    } else {
      alert("Movimentação registrada!");
    }
  }

  return (
    <div>
      <Navbar />

      {/* AGORA USANDO O CSS CERTO */}
      <div className="estoque-container">
        <h2>Gestão de Estoque</h2>

        <select
          className="estoque-select"
          value={produtoId}
          onChange={(e) => setProdutoId(e.target.value)}
        >
          <option value="">Selecione um produto</option>
          {produtos.map((p) => (
            <option key={p.id} value={p.id}>
              {p.nome}
            </option>
          ))}
        </select>

        <select
          className="estoque-select"
          value={tipo}
          onChange={(e) => setTipo(e.target.value)}
        >
          <option value="entrada">Entrada</option>
          <option value="saida">Saída</option>
        </select>

        <input
          className="estoque-input"
          type="number"
          placeholder="Quantidade"
          value={quantidade}
          onChange={(e) => setQuantidade(e.target.value)}
        />

        <input
          className="estoque-input"
          type="date"
          value={dataMov}
          onChange={(e) => setDataMov(e.target.value)}
        />

        <button className="estoque-button" onClick={enviar}>
          Confirmar Movimentação
        </button>
      </div>
    </div>
  );
}
