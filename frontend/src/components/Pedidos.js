import axios from "axios";
import { useState, useEffect, useMemo } from "react";
import { Styles } from "./Styles";
import { Table } from "./Table";

export default function Pedidos() {
  const [data, setData] = useState([]);
  const getPedidos = () => {
    axios
      .get("/api/pedidos")
      .then((res) => {
        if (res.data !== undefined) {
          setData(res.data);
          console.log("undefined sendo impresso")
        }
        console.log(" inside function: ");
        console.log(data);
      })
      .catch((e) => console.error(e));
  };

  const columns = useMemo(
    () => [
      { Header: "Cliente", accessor: "cod_cliente" },
      { Header: "Pedido", accessor: "numero_pedido" },
      { Header: "Cod Pedido", accessor: "cod_pedido" },
      { Header: "Etapa", accessor: "etapa" },
      { Header: "Cenario Fiscal", accessor: "cenario_fiscal" },
      { Header: "Produto", accessor: "codigo_produto" },
      { Header: "Quantidade", accessor: "quantidade" },
    ],
    []
  );
  useEffect(() => {
    getPedidos();
  }, []);

  return (
    <div>
      <h1>Pedidos</h1>
      <Styles>
        <p></p>
        <Table columns={columns} data={data} />
      </Styles>
    </div>
  );
}
