// src/components/LandingPage.js
import React from 'react';
import { Hero } from "./components/Hero";
import { Header } from "./components/Header";
import { Footer } from "./components/Footer";

const LandingPage = () => {
  return (
    <div className="landing-page">
      {/* Hero Section */}
      <Header />
      <Hero />
      <Footer />
    </div>
  );
};

export default LandingPage;
