import "../styles/ModalConfirm.css";

export default function ModalConfirm({ mensagem, onConfirm, onCancel }) {
  return (
    <div className="modal-overlay">
      <div className="modal-box">

        <p className="modal-text">{mensagem}</p>

        <div className="modal-buttons">
          <button className="modal-btn cancel" onClick={onCancel}>
            Cancelar
          </button>
          <button className="modal-btn confirm" onClick={onConfirm}>
            Confirmar
          </button>
        </div>

      </div>
    </div>
  );
}
