import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import RentalDetails from './RentalDetails';
import reportWebVitals from './reportWebVitals';

var rentalInfo = {name: 'Casa Era Ora', pic: "https://a0.muscache.com/im/pictures/3542b90c-d817-44ef-a4df-fef3578b2735.jpg?im_w=960",
  description: 'Entire home hosted by Marco',
  size: '6 guests 3 bedrooms 2 baths', id: 'bprxyx' };  

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
     <RentalDetails id={rentalInfo.id} name={rentalInfo.name} pic={rentalInfo.pic} 
      description={rentalInfo.description} size={rentalInfo.size} /> 
  </React.StrictMode> 
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
