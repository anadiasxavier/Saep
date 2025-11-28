const API_URL = "http://127.0.0.1:8000/api/";

// LOGIN
export async function login(email, senha) {
  const response = await fetch(API_URL + "login/", {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ email, senha }),
  });

  if (!response.ok) {
    return { erro: "Credenciais inválidas" };
  }

  return response.json();
}

// REQUEST COM TOKEN
export async function requestWithToken(url, method = "GET", body = null) {
  const token = localStorage.getItem("access") || "";

  // debug: ver token no console (remova depois)
  console.log("TOKEN ENVIADO:", token);

  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
      Authorization: token ? `Bearer ${token}` : "",
    },
  };

  if (body) {
    options.body = JSON.stringify(body);
  }

  const response = await fetch(API_URL + url, options);

  if (response.status === 401) {
    localStorage.removeItem("access");
    window.location.href = "/login";
    return { erro: "401" };
  }

  try {
    return await response.json();
  } catch (err) {
    return {};
  }
}

// produtos
export function getProdutos() {
  return requestWithToken("produtos/");
}
export function createProduto(prod) {
  return requestWithToken("produtos/", "POST", prod);
}
export function updateProduto(id, prod) {
  return requestWithToken(`produtos/${id}/`, "PUT", prod);
}
export function deleteProduto(id) {
  return requestWithToken(`produtos/${id}/`, "DELETE");
}

// estoque
export function movimentarEstoque(data) {
  return requestWithToken("movimentar/", "POST", data);
}
