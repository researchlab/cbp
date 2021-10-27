import React from 'react';
import ReactDOM from 'react-dom';
import './styles/default.scss';
import App from './app'
import store from './app/store'
import { Provider } from 'react-redux'

ReactDOM.render(
		<Provider store={store}>
			<App />
		</Provider>,
    document.getElementById('app')
)

if (module.hot){
    module.hot.accept()
}
