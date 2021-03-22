import useSWR from 'swr';
import { AppProps } from 'next/app';
import ReactTooltip from "react-tooltip";
import { useState } from 'react';
import WorldMap from '@/components/WorldMap';
import TableCovidStats from '@/components/TableCovidStats';
import Image from 'next/image';
import Head from 'next/head';
import '@/styles/global.css'
import IWorldMapStats from '@/interfaces/Components/WorldMap/IWorldMapStats.interface'
import CovidDataArray from '@/interfaces/Components/WorldMap/CovidDataArray.interface';
import styled from 'styled-components';


function App({ Component, pageProps }: AppProps) {
    const fetcher = (url: string) => fetch(url)
        .then(res => res.json());

    const { data, error } = useSWR<CovidDataArray>('http://127.0.0.1:8000/covidmap/get-todays-data/?format=json', fetcher);

    var dateToday = new Date();
    dateToday.setDate(dateToday.getDate() - 1);

    var [content, setContent] = useState("");
    var [worldStats, setWorldStats] = useState<IWorldMapStats>({
        dateRegistered: "01/01/1900",
        newCases: 0,
        newDeaths: 0,
        newTests: 0,
        newVaccinations: 0,
        totalCases: 0,
        totalDeaths: 0,
        peopleVaccinated: 0,
        populationDensity: 0,
        population: 0,
        humanDevelopmentIndex: 0,
        country: ""
        
    });

    const WIDTH = 1300;

    return (
        <div>
            <Head>
                <title>Covid World Map</title>
                <link rel="preconnect" href="https://fonts.gstatic.com" />
                <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500&display=swap" rel="stylesheet" />
            </Head>

            <body>
                <AppContainer
                    width={WIDTH}
                >
                    <nav className="navigation-bar">
                        <h1 className="noselect">Covid World Map</h1>
                    </nav>

                    <div className="content-container">

                        <WorldMap
                            data={data}
                            error={error}
                            setTooltipContent={setContent}
                            setWorldStats={setWorldStats}
                            width = {WIDTH}
                            />
                            
                        <ReactTooltip>{content}</ReactTooltip>

                        <TableCovidStats
                        worldStats={worldStats}
                        data ={ data}
                        error={error}
                        />
                    </div>

                </AppContainer>

            </body>


            <footer>
            Data for the day {`${dateToday.getDay().toString().padStart(2, "0")}/${dateToday.getMonth().toString().padStart(2, "0")}/${dateToday.getFullYear()}`} collected from Our World in Data.
            </footer>
        </div>
    )
}

const AppContainer = styled.div<{width: number}>`
.content-container {
    display: grid;
    grid-template-columns: ${props=>props.width}px auto;
    grid-template-rows: 1fr;
}

`

export default App;