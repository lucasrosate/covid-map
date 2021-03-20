import React, { memo } from "react";
import styled from 'styled-components';
import useSWR from 'swr';
import {
    ComposableMap,
    Geographies,
    Geography
} from "react-simple-maps";

import rounded from "@/utils/rounded";
import getRandomColor from '@/utils/getRandomColor';
import IWorldMapStats from '@/interfaces/Components/WorldMap/IWorldMapStats.interface';
import CovidDataArray from '@/interfaces/Components/WorldMap/CovidDataArray.interface';



const HEIGHT = 750;
const mapBasedColorPallette = "#296fca"
const geoUrl = "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

const randomColors = getRandomColor(mapBasedColorPallette, 193, 0.6);
const WorldMap: React.FC<{ data: CovidDataArray, error: string, setTooltipContent: React.SetStateAction<any>, setWorldStats: React.SetStateAction<any>, width?: number }>
    = ({ data, error, setTooltipContent, setWorldStats, width }) => {

        const WIDTH = width? width: 1300;

        return (
            <>
                {error && !data && <div className="failed-data">Failed. </div>}

                {!data && !error && <div className='loading-window'>Loading...</div>}

                {data && !error &&
                    <Container width={WIDTH} height={HEIGHT}>

                        <div className="worldmap-container">
                            <ComposableMap data-tip=""
                                projectionConfig={{ scale: 250 }}
            
                                width={WIDTH}
                                height={HEIGHT}
                            >
                                <Geographies geography={geoUrl}>
                                    {({ geographies }) =>
                                        geographies.map((geo, countryIndex) => (
                                            <Geography
                                                key={geo.rsmKey}
                                                geography={geo}
                                                onMouseEnter={() => {
                                                    const { NAME, NAME_LONG, POP_EST } = geo.properties;
                                                    

                                                    data.data_cases_countries.forEach((country, index) => {
                                                        if (country.location_name === NAME || country.location_name == NAME_LONG) {
                                                            setTooltipContent(`${NAME} — ${rounded(POP_EST)}`);
                                                            return;
                                                        }
                                                    });

                                                }}
                                                onClick={() => {
                                                    const { NAME, NAME_LONG, POP_EST } = geo.properties;

                                                    data.data_cases_countries.forEach((country, index) => {
                                                        if (country.location_name === NAME || country.location_name == NAME_LONG) {
                                                            let newWorldStats: IWorldMapStats = {
                                                                newCases: country.new_cases_smoothed,
                                                                newDeaths: country.new_deaths_smoothed,
                                                                newTests: country.new_tests_smoothed,
                                                                newVaccinations: country.new_vaccinations_smoothed,
                                                                totalCases: country.total_cases,
                                                                totalDeaths: country.total_deaths,
                                                                peopleVaccinated: country.people_vaccinated,
                                                                populationDensity: country.population_density,
                                                                population: POP_EST,
                                                                country: country.location_name
                                                            }

                                                            setWorldStats(newWorldStats);
                    
                                                            return;
                                                        }
                                                    });
                                                }}
                                                onMouseLeave={() => {
                                                    setTooltipContent("");
                                                }}
                                                style={{
                                                    default: {
                                                        fill: randomColors[countryIndex],
                                                        outline: "none"
                                                    },
                                                    hover: {
                                                        fill: "#3c7bce",
                                                        outline: "none"
                                                    },
                                                    pressed: {
                                                        fill: "#89b2e7",
                                                        outline: "none"
                                                    }
                                                }}
                                            />
                                        ))
                                    }
                                </Geographies>
                            </ComposableMap>
                        </div>
                    
                    </Container>
                }
                
            </>
        );
    };

const Container = styled.div<{width: number, height: number}>`

width: ${props=>props.width}px;
height: ${props=>props.height}px;
display: flex;
overflow: hidden;


margin-right: auto;

.rsm-svg {
        align-items: center;
        height: 100%;

}
`

export default memo(WorldMap);
