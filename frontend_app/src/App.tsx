import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Routes,
    Navigate,
} from "react-router-dom";

import "../styles/App.scss";

import Header from "./components/core/Header";
import Footer from "./components/core/Footer";
import MainAnonymous from "./components/core/MainAnonymous";
import MainAuth from "./components/core/MainAuth";

export const App = () => {
    return (
        <div className="wrapper">
            <Router>
                <header>
                    <Header />
                </header>
                <main>
                    <Routes>
                        <Route path="/auth" element={<MainAuth />} >AuthPage</ Route>
                        <Route path="/" element={<MainAnonymous />} />
                        <Route
                            path="/*"
                            element={<Navigate to={"/"} replace />}
                        />
                    </Routes>
                </main>
                <footer>
                    <Footer />
                </footer>
            </Router>
        </div>
    );
};
