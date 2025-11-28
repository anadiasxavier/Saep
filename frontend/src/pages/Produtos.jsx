import { useEffect, useState } from "react";
import { getProdutos, createProduto, updateProduto, deleteProduto } from "../api";
import Navbar from "../components/Navbar";
import ModalConfirm from "../components/Modal.Corfirm";
import "../styles/Produtos.css";

export default function Produtos() {
  const [produtos, setProdutos] = useState([]);
  const [busca, setBusca] = useState("");

  // Agora inclui quantidade_estoque e estoque_minimo
  const [form, setForm] = useState({
    nome: "",
    preco: "",
    quantidade_estoque: "",
    estoque_minimo: "",
  });

  const [editId, setEditId] = useState(null);

  const [modalOpen, setModalOpen] = useState(false);
  const [deleteId, setDeleteId] = useState(null);

  async function carregar() {
    const data = await getProdutos();
    const lista = Array.isArray(data) ? data : data.results || [];
    setProdutos(lista);
  }

  useEffect(() => {
    const token = localStorage.getItem("access");
    if (!token) return;
    carregar();
  }, []);

  async function salvar() {
    if (
      !form.nome ||
      !form.preco ||
      !form.quantidade_estoque ||
      !form.estoque_minimo
    ) {
      alert("Preencha todos os campos!");
      return;
    }

    if (editId) {
      await updateProduto(editId, form);
    } else {
      await createProduto(form);
    }

    setForm({
      nome: "",
      preco: "",
      quantidade_estoque: "",
      estoque_minimo: "",
    });

    setEditId(null);
    carregar();
  }

  function editar(p) {
    setEditId(p.id);
    setForm({
      nome: p.nome,
      preco: p.preco,
      quantidade_estoque: p.quantidade_estoque,
      estoque_minimo: p.estoque_minimo,
    });
  }

  function abrirModalExcluir(id) {
    setDeleteId(id);
    setModalOpen(true);
  }

  async function confirmarExclusao() {
    await deleteProduto(deleteId);
    setModalOpen(false);
    carregar();
  }

  return (
    <div>
      <Navbar />

      <div className="produtos-container">
        <h2>Cadastro de Produtos</h2>

        <input
          className="produtos-input"
          placeholder="Buscar..."
          value={busca}
          onChange={(e) => setBusca(e.target.value)}
        />

        <input
          className="produtos-input"
          placeholder="Nome"
          value={form.nome}
          onChange={(e) => setForm({ ...form, nome: e.target.value })}
        />

        <input
          className="produtos-input"
          placeholder="Preço"
          value={form.preco}
          onChange={(e) => setForm({ ...form, preco: e.target.value })}
        />

        <input
          className="produtos-input"
          placeholder="Quantidade em estoque"
          value={form.quantidade_estoque}
          onChange={(e) =>
            setForm({ ...form, quantidade_estoque: e.target.value })
          }
        />

        <input
          className="produtos-input"
          placeholder="Estoque mínimo"
          value={form.estoque_minimo}
          onChange={(e) =>
            setForm({ ...form, estoque_minimo: e.target.value })
          }
        />

        <button className="produtos-button" onClick={salvar}>
          {editId ? "Salvar Alterações" : "Cadastrar Produto"}
        </button>

        <table className="produtos-table">
          <thead>
            <tr>
              <th>Nome</th>
              <th>Preço</th>
              <th>Qtd</th>
              <th>Mínimo</th>
              <th>Ações</th>
            </tr>
          </thead>

          <tbody>
            {produtos
              .filter((p) =>
                p.nome.toLowerCase().includes(busca.toLowerCase())
              )
              .map((p) => (
                <tr key={p.id}>
                  <td>{p.nome}</td>
                  <td>{p.preco}</td>
                  <td>{p.quantidade_estoque}</td>
                  <td>{p.estoque_minimo}</td>

                  <td className="produtos-acoes">
                    <button onClick={() => editar(p)}>Editar</button>
                    <button onClick={() => abrirModalExcluir(p.id)}>
                      Excluir
                    </button>
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>

      {modalOpen && (
        <ModalConfirm
          mensagem="Tem certeza que deseja excluir este produto?"
          onConfirm={confirmarExclusao}
          onCancel={() => setModalOpen(false)}
        />
      )}
    </div>
  );
}
