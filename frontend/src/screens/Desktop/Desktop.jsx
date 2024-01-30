import React, { useState } from "react";
import { Input } from "../../components/Input";
import "./style.css";
import axios from 'axios';

export const Desktop = () => {
  const [file, setFile] = useState(null);
  const [bank, setBank] = useState(null);

  const handleBankChange = (event) => {
    setBank(event.target.value)
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    const formData = new FormData();
    formData.append('file', file);
    formData.append('bank', bank);

    await axios.post('http://localhost:8000/pdf_to_csv', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      responseType: "blob"
    }).then(response => {
      let url = window.URL.createObjectURL(response.data);
      let a = document.createElement('a');
      a.href = url;
      a.download = "data.csv";
      a.click();
    }).catch(err => console.log(err))

  };
  return (
    <div className="desktop">
      <div className="group-wrapper">
        <div className="group">
          <div className="div">Hosted by Jahn</div>
          <div className="overlap-group-wrapper">
            <div className="overlap-group">
              <form onSubmit={handleSubmit}>
                <p className="p">Converta seu extrato para um arquivo CSV</p>
                <div className="group-2">
                  <div className="group-3">
                    <div className="text-wrapper-2">Arquivo</div>
                    <Input className="input-instance" divClassName="design-component-instance-node" text="Nenhum selecionado" setFile={setFile} />
                  </div>
                  <div className="group-4">
                    <div className="text-wrapper-2">Banco de origem</div>
                    <div className="button-group">
                      <div className="button-left">
                        <label className="text-wrapper-3"><input type="radio" value="inter" onChange={handleBankChange} checked={bank === 'inter'} />Inter</label>
                      </div>
                      <div className="button-middle">
                        <label className="text-wrapper-4"><input type="radio" value="picpay" onChange={handleBankChange} checked={bank === 'picpay'} />PicPay</label>
                      </div>
                      <div className="button-right">
                        <label className="text-wrapper-5"><input type="radio" value="other" onChange={handleBankChange} checked={bank === 'other'} />Outro</label>
                      </div>
                    </div>
                  </div>
                  <button type="submit" className="button">
                    <div className="text-wrapper-6">Converter</div>
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
