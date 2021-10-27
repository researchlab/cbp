import React from 'react'
import './app.scss'
import Nums from './components/nums'
const image = require('./assets/images/logo.png')


function App(){
                 
	return <div className="page" >
    <div className="content" >
			<img src={image} />
			<h1>Fvx</h1>
			<Nums />
    </div>
  </div>

}

export default App
