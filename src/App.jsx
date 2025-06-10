// Custom styles 
import "./styles.css";
// React imports
import { useEffect } from 'react';
import { Routes, Route } from "react-router-dom";
import { useNavigate } from 'react-router-dom';
// Components
import AboutUs from "./components/AboutUs";
import AdoptionForm from "./components/AdoptionForm";
import ApplicationDetail from "./components/ApplicationDetail";
import Applications from "./components/Applications";
import Confirmation from "./components/Confirmation";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Home from "./components/Home";
import Pets from "./components/Pets";

function App() {
  const navigate = useNavigate();

  return (
    <div className="wrapper">
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<AboutUs />} />
          <Route path="/adopt" element={<AdoptionForm />} />
          <Route path="/confirmation" element={<Confirmation />} />
          <Route path="/error" element={<Error />} />
          <Route path="/pets" element={<Pets />} />
          <Route path="/applications" element={<Applications />} />
          <Route path="/applications/:id" element={<ApplicationDetail />} />
          <Route path="*" element={<div className='home'><h2>Page Not Found</h2></div>} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export default App;
