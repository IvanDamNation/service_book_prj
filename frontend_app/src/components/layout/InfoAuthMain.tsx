import React, { useEffect, useState } from "react";

import TableInfo from "../reusable/TableInfo";
import NavAuth from "../reusable/NavAuth";
import { IMachine } from "../../types/machine/machine";
import axios from "axios";
// import Raw from "../reusable/table_components/Raw";
import List from "../reusable/List";


const InfoAuthMain = () => {
    const [machines, setMachines] = useState<IMachine[]>([]);

    useEffect(() => {
        fetchInfo()
    }, []);

    async function fetchInfo () {
        try {
            const response = await axios.get<IMachine[]>(
                "http://127.0.0.1:8000/service_center/get_machine"
            );
            setMachines(response.data);
        } catch (e) {
            alert(e)
        }
    }

    const colNames = [
        'pk', "Серийный номер", "Модель", "Двигатель", "Номер двигателя", 
        "Трансмиссия", "Номер трансмиссии", 'Модель ведущего моста', 
        'Зав. № ведущего моста', 'Модель управляемого моста', 
        'Зав. № управляемого моста', 'Договор поставки №, дата',
        'Дата отгрузки с завода', 'Грузополучатель (конечный потребитель)',
        'Адрес поставки (эксплуатации)', 'Комплектация (доп. опции)',
        'Клиент', 'Сервисная компания'
    ]

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
                <TableInfo machines={machines} colNames={colNames}/>
            </div>
        </div>
    );
}

export default InfoAuthMain;