import React from "react";

import TableInfo from "../reusable/TableInfo";
import SearchByNumber from "../reusable/SearchByNumber";


const MainAnonymous = () => {
    return (
        <div className="contentAnonim">
            <p className="mainInfo">
                Проверьте комплектацию и технические характеристики техники
                Силант
            </p>
            <SearchByNumber />
            <p className="searchResult">Результат поиска:</p>
            <div className="searchInfo">
                <h2 className="searchInfoHead">
                    Информация о комплектации и технических характеристиках
                    Вашей техники
                </h2>
                <TableInfo />
            </div>
        </div>
    );
};

export default MainAnonymous;