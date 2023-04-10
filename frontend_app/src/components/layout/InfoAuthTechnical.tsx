import { useEffect, useState } from "react";

import TableInfo from "../reusable/TableInfo";
import NavAuth from "../reusable/NavAuth";
import { IMaintenance } from "../../types/machine/maintenance";
import axios from "axios";


const InfoAuthTechnical = () => {
    const [maintenance, setMaintenance] = useState<IMaintenance[]>([]);

    useEffect(() => {
        fetchInfo()
    }, []);

    async function fetchInfo () {
        try {
            const response = await axios.get<IMaintenance[]>(
                "http://127.0.0.1:8000/service_center/maintenance/"
            );
            setMaintenance(response.data);
        } catch (e) {
            alert(e)
        }
    }
    
    const colNames = [
        "#", "Вид ТО", "Дата проведения ТО", "Наработка, м/час",
        "№ заказ-наряда", "Дата заказ-наряда", "Организация, проводившая ТО",
        "Машина", "Сервисная компания"
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
                <TableInfo mainProps={maintenance} colNames={colNames}/>
            </div>
        </div>
    );
}

export default InfoAuthTechnical;
