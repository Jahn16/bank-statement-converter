import React, { useState } from "react";
import { Input } from "../../components/Input";
import "./style.css";
import axios from 'axios';

export const Desktop = () => {
  const [file, setFile] = useState(null);
  const [bank, setBank] = useState(null);

  const handleBankChange = (event) => {
    if (event.target.value === "picpay") {
      alert("Suporte para PicPay ainda está em desenvolvimento")
      return
    }
    else if (event.target.value === "other") {
      alert("Sugira um novo banco a ser adicionado por meio de um issue no GitHub https://github.com/Jahn16/bank-statement-to-csv")
      return
    }
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
    }).then(response => {
      let blob = new Blob([response.data])
      let url = window.URL.createObjectURL(blob);
      let a = document.createElement('a');
      a.href = url;
      a.download = "data.csv";
      a.click();
    }).catch(err => {
      if(err.response.status >= 400 && err.response.status < 500){
        alert(err.response.data.detail)
        return
      }
      alert("Um erro interno ocorreu")

    })

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
