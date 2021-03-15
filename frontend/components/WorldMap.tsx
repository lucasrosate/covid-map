import React, { memo } from "react";
import styled from 'styled-components';
import useSWR from 'swr';
import {
    ComposableMap,
    Geographies,
    Geography
} from "react-simple-maps";

import rounded from "@/utils/rounded";

import IWorldMapStats from '@/interfaces/Components/WorldMap/IWorldMapStats.interface';
import CovidDataArray from '@/interfaces/Components/WorldMap/CovidDataArray.interface';


const geoUrl =
    "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";


const WorldMap: React.FC<{ setTooltipContent: React.SetStateAction<any>, setWorldStats: React.SetStateAction<any> }>
    = ({ setTooltipContent, setWorldStats }) => {

        const fetcher = (url: string) => fetch(url)
            .then(res => res.json());

        const { data, error } = useSWR<CovidDataArray>('http://127.0.0.1:8000/covidmap/get-todays-data/?format=json', fetcher);

        return (
            <>
                {error && !data && <div className="failed-data">Failed. </div>}

                {!data && !error && <div className='loading-window'>Loading...</div>}

                {
                    <Container>
                        <div className="worldmap-container">
                            <ComposableMap data-tip=""
                            projectionConfig={{ scale: 0 }}
                            height={600}
                            width={900}
                            >
                                <Geographies geography={geoUrl}>
                                    {({ geographies }) =>
                                        geographies.map((geo,index) => (
                                            <Geography
                                                key={geo.rsmKey}
                                                geography={geo}
                                                onMouseEnter={() => {
                                                    const { NAME, NAME_LONG, POP_EST } = geo.properties;

                                                    let newCases: number;
                                                    let newDeaths: number;
                                                    let newTests: number;
                                                    let newVaccinations: number;
                                                    let totalCases: number;
                                                    let totalDeaths: number;
                                                    let peopleVaccinated: number;
                                                    let populationDensity: number;

                                                    data.data_cases_countries.forEach((country) => {
                                                        if (country.location_name === NAME || country.location_name == NAME_LONG) {

                                                            let newWorldStats: IWorldMapStats = {
                                                                newCases: country.new_cases_smoothed,
                                                                newDeaths: country.new_deaths_smoothed,
                                                                newTests: country.new_tests_smoothed,
                                                                newVaccinations: country.new_vaccinations_smoothed,
                                                                totalCases: country.total_cases,
                                                                totalDeaths: country.total_deaths,
                                                                peopleVaccinated: country.people_vaccinated,
                                                                populationDensity: country.population_density
                                                            }

                                                            setWorldStats(newWorldStats);
                                                            setTooltipContent(`${NAME} — ${rounded(POP_EST)}`);
                                                            return;
                                                        }
                                                    });


                                                }}
                                                onMouseLeave={() => {
                                                    setTooltipContent("");
                                                }}
                                                style={{
                                                    default: {
                                                        fill: "red",
                                                        outline: "none"
                                                    },
                                                    hover: {
                                                        fill: "#F53",
                                                        outline: "none"
                                                    },
                                                    pressed: {
                                                        fill: "#E42",
                                                        outline: "none"
                                                    }
                                                }}
                                            />
                                        ))
                                    }
                                </Geographies>
                            </ComposableMap>
                        </div>


                        {/* {JSON.stringify(data)} */}
                    </Container>
                }

            </>
        );
    };

const Container = styled.div`

width: 80%;
height: 600px;
display: flex;
overflow: hidden;

.worldmap-container {
    margin-left: auto;
    margin-right: auto;

    svg {
        height: 100%;
        margin-left: auto;
        margin-right: auto;
    }
}

`

export default memo(WorldMap);
