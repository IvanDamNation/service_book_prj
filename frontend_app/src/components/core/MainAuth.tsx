import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Routes,
    Navigate,
} from "react-router-dom";

import Description from "../reusable/Description";
import InfoAuthMain from "../layout/InfoAuthMain";
import InfoAuthTechnical from "../layout/InfoAuthTechnical";


const MainAuth = () => {
    return (
        <div className="contentAuth">
                <InfoAuthMain />
                <InfoAuthTechnical />
                <Description />
        </div>
    );
}

export default MainAuth;