import React from "react";
import "../styles/App.scss";

import Header from "./components/core/Header";
import Footer from "./components/core/Footer";
import MainAnonymous from "./components/core/MainAnonymous";
import MainAuth from "./components/core/MainAuth";


export const App = () => {
    return (
        <div className="wrapper">
            <header>
                <Header />
            </header>
            <main>
                <MainAnonymous />
                <MainAuth />
            </main>
            <footer>
                <Footer />
            </footer>
        </div>
    );
};
