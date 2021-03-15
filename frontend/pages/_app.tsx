import useSWR from 'swr';
import { AppProps } from 'next/app';
import ReactTooltip from "react-tooltip";
import { useState } from 'react';
import WorldMap from '@/components/WorldMap';
import Image from 'next/image';
import Head from 'next/head';
import '@/styles/global.css'
import IWorldMapStats from '@/interfaces/Components/WorldMap/IWorldMapStats.interface'


function App({ Component, pageProps }: AppProps) {

    var [content, setContent] = useState("");
    var [worldStats, setWorldStats] = useState<IWorldMapStats>({
        newCases: 0,
        newDeaths: 0,
        newTests: 0,
        newVaccinations: 0,
        totalCases: 0,
        totalDeaths: 0,
        peopleVaccinated: 0,
        populationDensity: 0,
    });
    
    return (
        <div>
            <Head>
                <title>Covid World Map</title>
                <link rel="preconnect" href="https://fonts.gstatic.com" />
                <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500&display=swap" rel="stylesheet" />
            </Head>

            <body>
                <nav>
                    <h1>Covid World Map
                        <span className="nav-image">
                            <Image
                                src="/nav/world.svg"
                                alt="world"
                                width={28}
                                height={28}
                            />
                        </span>

                    </h1>
                </nav>

                <WorldMap
                setTooltipContent={setContent}           
                setWorldStats={setWorldStats}/>
                
                <ReactTooltip>{content}</ReactTooltip>
            </body>
        </div>
    )


}

export default App;