import rounded from '@/utils/rounded';
import thousandSeparator from '@/utils/thousandSeparator';
import ICovidData from '@/interfaces/Components/WorldMap/IWorldMapStats.interface';
import CovidDataArray from '@/interfaces/Components/WorldMap/CovidDataArray.interface';

import styled from 'styled-components';
const TableCovidStats: React.FC<{ worldStats: ICovidData, data:CovidDataArray,  error: string }> = ({ worldStats, data, error }) => {


    return (
        <>
            {error && !data && <div className="failed-data">Failed. </div>}

            {!data && !error && <div className='loading-window'>Loading...</div>}

            {data && !error && worldStats.country.length > 0 && 
                <TableContainer>
                    <h1>{worldStats.country}</h1>
                    <div className="data-container">

                    <tr>
                        <td>Population:</td>
                        <td>{thousandSeparator(worldStats.population)}</td>
                    </tr>

                    <tr>
                        <td>New Cases:</td>
                        <td>{thousandSeparator(worldStats.newCases)}</td>
                    </tr>

                    <tr>
                        <td>New Deaths:</td>
                        <td>{thousandSeparator(worldStats.newDeaths)}</td>
                    </tr>

                    <tr>
                        <td>New Vaccinations:</td>
                        <td>{thousandSeparator(worldStats.newVaccinations)}</td>
                    </tr>

                    <tr>
                        <td>Total Cases:</td>
                        <td>{thousandSeparator(worldStats.totalCases)}</td>
                    </tr>

                    <tr>
                        <td>Total Deaths:</td>
                        <td>{thousandSeparator(worldStats.totalDeaths)}</td>
                    </tr>

                    <tr>
                        <td>Total Vaccinated:</td>
                        <td>{thousandSeparator(worldStats.peopleVaccinated)}</td>
                    </tr>

                    <tr>
                        <td>Population Density:</td>
                        <td>{worldStats.populationDensity} hab/km²</td>
                    </tr>
                    


                    </div>
                </TableContainer>
            }
        </>


    )
}

export default TableCovidStats;


const TableContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;

    

    margin-top: 100px;
    margin-right: 40px;
    
    h1 {
        text-align: center;
        color: var(--primary-color);
        font-size: 1.6rem;
    }

    .data-container {
        padding: 18px 35px;
        border-radius: 8px;
        background-color: rgb(235, 235, 235);
        height: auto;
        width: 100%;

        font-size: 120%;

        tr {
            height: 40px;
            
            td:first-child {
                font-weight: 500;
                color: rgb(50, 50, 50);
            }
            
            td:nth-child(2) {
                padding-left: 20px;
                font-weight: 300;
            }
        }



    }
`