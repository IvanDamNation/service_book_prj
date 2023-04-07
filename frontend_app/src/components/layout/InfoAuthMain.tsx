import React from "react";

import TableInfo from "../reusable/TableInfo";
import NavAuth from "../reusable/NavAuth";


const InfoAuthMain = () => {
    return (
        <div className="contentAuthMainInfo">
            <p className="mainInfo">Основная панель</p>
            <div className="headerDown">
                <h2>Клиент/Сервисная компания (от кого авторизовались)</h2>
            </div>
            <div className="searchInfo">
                <div className="searchInfoHeadContainer"></div>
                <h2 className="searchInfoHead">
                    Информация о комплектации и технических характеристиках
                    Вашей техники
                </h2>
                <NavAuth />
                <TableInfo />
            </div>
        </div>
    );
}

export default InfoAuthMain;