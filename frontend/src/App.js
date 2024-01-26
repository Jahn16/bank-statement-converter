import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [file, setFile] = useState("");
  const [bank, setBank] = useState("");

  const submitFile = async () => {
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

  const onFileChange = e => {
    setFile(e.target.files[0]);
  };

  const onBankChange = e => {
    setBank(e.target.value);
  };

  return (
    <div>
      <input type="file" accept="application/pdf" onChange={onFileChange} />
      <input type="text" placeholder="Bank Name" onChange={onBankChange} />
      <button onClick={submitFile}>Submit</button>
    </div>
  );
}

export default App;
