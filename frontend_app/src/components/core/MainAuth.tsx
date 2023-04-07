import React from "react";

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