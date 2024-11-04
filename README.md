# EnvGuard-2024.github.io

## Dataset

We collected data in each of the two real-world WoT environments and built a dataset to evaluate EnvGuard. The dataset is publicly available.  
The dataset for the building environment is as follows:  
([Building Dataset](https://github.com/EnvGuard-2024/EnvGuard-2024.github.io/tree/master/DataSet/BuildingEnvironment))  
The dataset for the home environment is as follows:  
([Home Dataset](https://github.com/EnvGuard-2024/EnvGuard-2024.github.io/tree/master/DataSet/HomeEnvironment))

<p> 
We conducted a 28-day continuous data collection in the intelligent building and smart home, recording user activities, application executions and environment changes by capturing every event and action from the initial environment state.  
The spatial layout and the deployed devices of the intelligent building and the smart home are illustrated as follows:  
<div align=center>
<img width="80%" src="https://raw.githubusercontent.com/EnvGuard-2024/EnvGuard-2024.github.io/master/images/new_layout.png"/>
</div>
</p>

We deployed 17 WoT applications in building for daily office work and 18 WoT applications in home for home life. The applications are as follows:

<div align=center> 
<img width="48%" style="margin-right:2%" src="https://raw.githubusercontent.com/EnvGuard-2024/EnvGuard-2024.github.io/master/images/office_application.png"/>
<img width="50.5%" src="https://raw.githubusercontent.com/EnvGuard-2024/EnvGuard-2024.github.io/master/images/home_application.png"/> 
</div>

we summarize ten real-world safety and security property requirements according to online accident reports and offline interviews with owners and individuals. Ten of them involve spatial state (#1 to #5 and #11 to #15), and the rest ten involve temporal trace. We then invited four experts with WoT development experience to independently analyze and label the events and actions that violated the properties (Fleiss Kappa = 0.71) and resolve discrepancies through discussion to obtain the ground truth. The properties are as follows:

<div align=center>
<img width="70%" src="https://raw.githubusercontent.com/EnvGuard-2024/EnvGuard-2024.github.io/master/images/propertys.png"/>
</div>

The dataset includes the initial state of the environment and devices, and the state changes during the following 28 days which are recorded in the formats: {Name, Type, Location, Object, Timestamp, Payload Data, Source, Property Violation, Resolving Action}. Name indicates the name of device service that provides information about changes in the state of the environment/device. Type represents the type (action or event) of the device service. Location indicates the deployment location of the device. Object denotes the state name of the target device/environment object being updated by the device service. Timestamp records the time when the state change occurs. Source indicates that the data record is caused by an environment change, an application call, or an offline user operation. Payload Data records the current state value. Property Violation indicates the ID of violated environment properties caused by the device service. Resolving Action indicates the generated resolving strategy of the violation.

## GUI Tool

The visualized environment property description tool.([GUI](http://47.101.169.122:9033/))

<div align=center> 
<img width="98%" src="https://raw.githubusercontent.com/EnvGuard-2024/EnvGuard-2024.github.io/master/images/GUI.png"/>
</div>

## Environment Representations

The environment representation of the intelligent building WoT environment in [neo4j](http://47.101.169.122:7474/browser/) (bolt port: `7687`, username: `neo4j`, password: `12345678`)  
The environment representation of the smart home WoT environment in [neo4j](http://47.101.169.122:7475/browser/) (bolt port: `7688`, username: `neo4j`, password: `12345678`)

## User Study 1

We invited 139 participants from both online media (91 people) and offline on-campus recruitment(48 people), including individuals who work or live daily in the building (23 people) and home (3 people) environments. In terms of diversity among participants, 78 are males and 61 are females, aged 23 to 47, with educational backgrounds from bachelor’s to doctoral degrees across various fields such as computer, chemistry, and art. To address ethical concerns, we ensured that all individuals and owners in both environments consented to the use and release of the environment information and collected device data. For participants, we confirmed their awareness of the ongoing survey and obtained their consent. Additionally, we manually reviewed the data and anonymized all sensitive information that may compromise privacy.  
The survey questionnair is as follows:  
([User Study 1](https://github.com/EnvGuard-2024/EnvGuard-2024.github.io/blob/master/UserStudy/UserStudyOne_SurveyQuestionnair.docx))

## User Study 2

We re-invite the 48 participants recruited offline in the previous user study to specify the properties for each environment using the property description tool. As none of them possess experience in WoT development, they can be considered as end users. We record the time cost for property customization and evaluate the accuracy of the customized properties. To further evaluate how much the abstract property templates help simplify property customization, we randomly divide all participants into two equal groups. Participants in group A are allowed to customize properties by describing the abstract device effect. In contrast, participants in group B could only define the states of device and space instances to construct properties.  
The results of the survey in the intelligent building are as follows:  
([Building-User Study 2](https://github.com/EnvGuard-2024/EnvGuard-2024.github.io/blob/master/UserStudy/UserStudyTwo_ConstructedProperties_Office.json))  
The results of the survey in the smart home are as follows:  
([Home-User Study 2](https://github.com/EnvGuard-2024/EnvGuard-2024.github.io/blob/master/UserStudy/UserStudyTwo_ConstructedProperties_Home.json))

## Code

All the experimental data and source code of our work is available: ([Code](https://github.com/EnvGuard-2024/EnvGuard-2024.github.io/blob/master/Code/))
