import React from "react";

const NavAuth = () => {
    return (
        <div className="infoNavContainer">
            <ul className="infoNav">
                <li>
                    <button className="mainInfoBtn">Общая инфо</button>
                </li>
                <li>
                    <button className="mainInfoBtn">Техобслуживание</button>
                </li>
                <li>
                    <button className="mainInfoBtn">Рекламации</button>
                </li>
            </ul>
        </div>
    );
}

export default NavAuth;