import React from "react";

import TableInfo from "../reusable/TableInfo";
import NavAuth from "../reusable/NavAuth";
import { IMachine } from "../../types/machine/machine";




const InfoAuthTechnical = () => {
    return (
        <div className="contentAuthTechnical">
                <p className="mainInfo">Основная панель</p>
                <div className="headerTechnical">
                    <h3 className="headerTechnicalInfo">Машина 1</h3>
                    <h4 className="headerTechnicalInfo">Заводской номер</h4>
                </div>
                <div className="searchInfo">
                    <div className="searchInfoHeadContainer"></div>
                    <h2 className="searchInfoHead">
                        Информация о проведении технического обслуживания Вашей
                        техники
                    </h2>
                    <NavAuth />
                    {/* <TableInfo /> */}
                </div>
            </div>
    );
}

export default InfoAuthTechnical;