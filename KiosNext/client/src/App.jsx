import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import {StockTotal} from './pages/StockTotal';
import {Stockear} from './pages/Stockear';

import { Navigations } from './components/navigations';

import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';

function App() {
    return (
      <BrowserRouter>
        <Navigations />
        <Routes>
          <Route path='/' element={<Navigate to={'/stock'} />} />
          <Route path='/stock' element={<StockTotal />} />
          <Route path='/stockear' element={<Stockear />} />
        </Routes>
      </BrowserRouter>
    );
}

export default App;