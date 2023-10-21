import React, { useState } from 'react';

// material-ui
import Container from '@mui/material/Container';
import Timeline from '@mui/lab/Timeline';
import TimelineItem, { timelineItemClasses } from '@mui/lab/TimelineItem';
import TimelineSeparator from '@mui/lab/TimelineSeparator';
import TimelineConnector from '@mui/lab/TimelineConnector';
import TimelineContent from '@mui/lab/TimelineContent';
import TimelineDot from '@mui/lab/TimelineDot';
import Typography from '@mui/material/Typography';

// project import
import MainCard from '../../components/MainCard';

// assets
import { SearchOutlined } from '@ant-design/icons';

const ApplicationsHelp = () => {

    return (
        <MainCard title='Información' >

            <Container>
                <Typography variant="body1" color="text.primary" >
                    Estos son los diferentes estados en los que puedes estar:
                </Typography>

                <Timeline position="right"
                    sx={{
                        [`& .${timelineItemClasses.root}:before`]: {
                            flex: 0,
                            padding: 0,
                        },
                    }}
                >
                    <TimelineItem>
                        <TimelineSeparator>
                            <TimelineDot variant="filled" color="secondary" />
                            <TimelineConnector />
                        </TimelineSeparator>
                        <TimelineContent>Postulado</TimelineContent>
                    </TimelineItem>
                    <TimelineItem>
                        <TimelineSeparator>
                            <TimelineDot variant="filled" color="primary" />
                            <TimelineConnector />
                        </TimelineSeparator>
                        <TimelineContent>Assessment completado</TimelineContent>
                    </TimelineItem>
                    <TimelineItem>
                        <TimelineSeparator>
                            <TimelineDot variant="filled" color="warning" />
                            <TimelineConnector />
                        </TimelineSeparator>
                        <TimelineContent>Evaluado</TimelineContent>
                    </TimelineItem>
                    <TimelineItem>
                        <TimelineSeparator>
                            <TimelineDot variant="filled" color="success" />
                        </TimelineSeparator>
                        <TimelineContent>Proceso finalizado</TimelineContent>
                    </TimelineItem>
                </Timeline>
            </Container>

        </MainCard>
    )
}

export default ApplicationsHelp;