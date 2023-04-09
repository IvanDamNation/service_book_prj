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
import InfoAuthComplaint from "../layout/InfoAuthComplaint";


const MainAuth = () => {
    return (
        <div className="contentAuth">
                <InfoAuthMain />
                <InfoAuthTechnical />
                <InfoAuthComplaint />
                <Description />
        </div>
    );
}

export default MainAuth;