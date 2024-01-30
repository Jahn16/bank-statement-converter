/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React, { useState } from 'react';
import "./style.css";

export const Input = ({
  showHelpText = false,
  helpText = "Sample text",
  selectArrow = true,
  endAdornment = false,
  text = "Nenhum selecionado",
  showStartAdornment = false,
  showLabel = false,
  className,
  divClassName,
  setFile,
}) => {
  const [filename, setFilename] = useState(null);
  const handleFileChange = (event) => {
    setFilename(event.target.files[0].name)
    setFile(event.target.files[0]);
  };
  return (
    <div className={`input ${className}`}>
      <div className="content">
        <div className="input-wrapping">
          <div className="div-wrapper">
            <label className="text-wrapper">
              Escolher arquivo
              <input
                type="file"
                style={{ display: 'none' }}
                onChange={handleFileChange}
              />
            </label>

          </div>
        </div>
        <div className={`nenhum-selecionado ${divClassName}`}>{filename? filename.substr(0, 25) : text}</div>
      </div>
    </div>
  );
};

Input.propTypes = {
  showHelpText: PropTypes.bool,
  helpText: PropTypes.string,
  selectArrow: PropTypes.bool,
  endAdornment: PropTypes.bool,
  text: PropTypes.string,
  showStartAdornment: PropTypes.bool,
  showLabel: PropTypes.bool,
};
