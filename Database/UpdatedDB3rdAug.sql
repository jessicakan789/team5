-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: population
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cutdownpopulation`
--

DROP TABLE IF EXISTS `cutdownpopulation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cutdownpopulation` (
  `Area` text,
  `Locality Type` text,
  `Population` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cutdownpopulation`
--

LOCK TABLES `cutdownpopulation` WRITE;
/*!40000 ALTER TABLE `cutdownpopulation` DISABLE KEYS */;
INSERT INTO `cutdownpopulation` VALUES ('UNITED KINGDOM','Country',67081234),('ENGLAND','Country',56550138),('County Durham','Unitary Authority',533149),('Darlington','Unitary Authority',107402),('Hartlepool','Unitary Authority',93836),('Middlesbrough','Unitary Authority',141285),('Northumberland','Unitary Authority',323820),('Redcar and Cleveland','Unitary Authority',137228),('Stockton-on-Tees','Unitary Authority',197419),('Gateshead','Metropolitan District',201950),('Newcastle upon Tyne','Metropolitan District',306824),('North Tyneside','Metropolitan District',208871),('South Tyneside','Metropolitan District',151133),('Sunderland','Metropolitan District',277846),('Blackburn with Darwen','Unitary Authority',150030),('Blackpool','Unitary Authority',138381),('Cheshire East','Unitary Authority',386667),('Cheshire West and Chester','Unitary Authority',343823),('Halton','Unitary Authority',129759),('Warrington','Unitary Authority',209397),('Cumbria','County',499781),('Bolton','Metropolitan District',288248),('Bury','Metropolitan District',190708),('Manchester','Metropolitan District',555741),('Oldham','Metropolitan District',237628),('Rochdale','Metropolitan District',223659),('Salford','Metropolitan District',262697),('Stockport','Metropolitan District',294197),('Tameside','Metropolitan District',227117),('Trafford','Metropolitan District',237579),('Wigan','Metropolitan District',330712),('Lancashire','County',1227076),('Knowsley','Metropolitan District',152452),('Liverpool','Metropolitan District',500474),('Sefton','Metropolitan District',275899),('St. Helens','Metropolitan District',181095),('Wirral','Metropolitan District',324336),('East Riding of Yorkshire','Unitary Authority',343201),('Kingston upon Hull, City of','Unitary Authority',259126),('North East Lincolnshire','Unitary Authority',159364),('North Lincolnshire','Unitary Authority',172748),('York','Unitary Authority',211012),('North Yorkshire','County',620610),('Barnsley','Metropolitan District',248071),('Doncaster','Metropolitan District',312785),('Rotherham','Metropolitan District',264984),('Sheffield','Metropolitan District',589214),('Bradford','Metropolitan District',542128),('Calderdale','Metropolitan District',211439),('Kirklees','Metropolitan District',441290),('Leeds','Metropolitan District',798786),('Wakefield','Metropolitan District',351592),('Derby','Unitary Authority',256814),('Leicester','Unitary Authority',354036),('Nottingham','Unitary Authority',337098),('Rutland','Unitary Authority',40476),('Derbyshire','County',807183),('Leicestershire','County',713085),('Lincolnshire','County',766333),('Nottinghamshire','County',833377),('Herefordshire, County of','Unitary Authority',193615),('Shropshire','Unitary Authority',325415),('Stoke-on-Trent','Unitary Authority',256622),('Telford and Wrekin','Unitary Authority',181322),('Staffordshire','County',883172),('Warwickshire','County',583786),('Birmingham','Metropolitan District',1140525),('Coventry','Metropolitan District',379387),('Dudley','Metropolitan District',322363),('Sandwell','Metropolitan District',329042),('Solihull','Metropolitan District',217487),('Walsall','Metropolitan District',286716),('Wolverhampton','Metropolitan District',264407),('Worcestershire','County',598070),('Bedford','Unitary Authority',174687),('Central Bedfordshire','Unitary Authority',294096),('Luton','Unitary Authority',213528),('Peterborough','Unitary Authority',202626),('Southend-on-Sea','Unitary Authority',182773),('Thurrock','Unitary Authority',175531),('Cambridgeshire','County',657204),('Essex','County',1497759),('Hertfordshire','County',1195672),('Norfolk','County',914039),('Suffolk','County',761246),('Camden','London Borough',279516),('Hammersmith and Fulham','London Borough',183544),('Haringey','London Borough',266357),('Islington','London Borough',248115),('Kensington and Chelsea','London Borough',156864),('Lambeth','London Borough',321813),('Lewisham','London Borough',305309),('Newham','London Borough',355266),('Southwark','London Borough',320017),('Tower Hamlets','London Borough',331969),('Wandsworth','London Borough',329735),('Westminster','London Borough',269848),('Barking and Dagenham','London Borough',214107),('Barnet','London Borough',399007),('Bexley','London Borough',249301),('Brent','London Borough',327753),('Bromley','London Borough',332752),('Croydon','London Borough',388563),('Ealing','London Borough',340341),('Enfield','London Borough',333587),('Greenwich','London Borough',289034),('Harrow','London Borough',252338),('Havering','London Borough',260651),('Hillingdon','London Borough',309014),('Hounslow','London Borough',271767),('Kingston upon Thames','London Borough',179142),('Merton','London Borough',206453),('Redbridge','London Borough',305658),('Richmond upon Thames','London Borough',198141),('Sutton','London Borough',207707),('Waltham Forest','London Borough',276940),('Bracknell Forest','Unitary Authority',124165),('Brighton and Hove','Unitary Authority',291738),('Buckinghamshire','Unitary Authority',547060),('Isle of Wight','Unitary Authority',142296),('Medway','Unitary Authority',279142),('Milton Keynes','Unitary Authority',270203),('Portsmouth','Unitary Authority',214692),('Reading','Unitary Authority',160337),('Slough','Unitary Authority',149577),('Southampton','Unitary Authority',252872),('West Berkshire','Unitary Authority',158465),('Windsor and Maidenhead','Unitary Authority',151273),('Wokingham','Unitary Authority',173945),('East Sussex','County',558852),('Hampshire','County',1389206),('Kent','County',1589057),('Oxfordshire','County',696880),('Surrey','County',1199870),('West Sussex','County',867635),('Bath and North East Somerset','Unitary Authority',196357),('Bournemouth, Christchurch and Poole','Unitary Authority',396989),('Bristol, City of','Unitary Authority',465866),('Dorset','Unitary Authority',379791),('North Somerset','Unitary Authority',215574),('Plymouth','Unitary Authority',262839),('South Gloucestershire','Unitary Authority',287816),('Swindon','Unitary Authority',222881),('Torbay','Unitary Authority',136218),('Wiltshire','Unitary Authority',504070),('Devon','County',810716),('Gloucestershire','County',640650),('Somerset','County',563851),('WALES','Country',3169586),('Isle of Anglesey','Unitary Authority',70440),('Gwynedd','Unitary Authority',125171),('Conwy','Unitary Authority',118184),('Denbighshire','Unitary Authority',96664),('Flintshire','Unitary Authority',156847),('Wrexham','Unitary Authority',136055),('Powys','Unitary Authority',133030),('Ceredigion','Unitary Authority',72895),('Pembrokeshire','Unitary Authority',126751),('Carmarthenshire','Unitary Authority',190073),('Swansea','Unitary Authority',246563),('Neath Port Talbot','Unitary Authority',144386),('Bridgend','Unitary Authority',147539),('Vale of Glamorgan','Unitary Authority',135295),('Cardiff','Unitary Authority',369202),('Rhondda Cynon Taf','Unitary Authority',241873),('Merthyr Tydfil','Unitary Authority',60424),('Caerphilly','Unitary Authority',181731),('Blaenau Gwent','Unitary Authority',70020),('Torfaen','Unitary Authority',94832),('Monmouthshire','Unitary Authority',95164),('Newport','Unitary Authority',156447),('SCOTLAND','Country',5466000),('Aberdeen City','Council Area',229060),('Aberdeenshire','Council Area',260780),('Angus','Council Area',115820),('Argyll and Bute','Council Area',85430),('City of Edinburgh','Council Area',527620),('Clackmannanshire','Council Area',51290),('Dumfries and Galloway','Council Area',148290),('Dundee City','Council Area',148820),('East Ayrshire','Council Area',121600),('East Dunbartonshire','Council Area',108750),('East Lothian','Council Area',107900),('East Renfrewshire','Council Area',96060),('Falkirk','Council Area',160560),('Fife','Council Area',374130),('Glasgow City','Council Area',635640),('Highland','Council Area',235430),('Inverclyde','Council Area',77060),('Midlothian','Council Area',93150),('Moray','Council Area',95710),('Na h-Eileanan Siar','Council Area',26500),('North Ayrshire','Council Area',134250),('North Lanarkshire','Council Area',341140),('Orkney Islands','Council Area',22400),('Perth and Kinross','Council Area',151910),('Renfrewshire','Council Area',179390),('Scottish Borders','Council Area',115240),('Shetland Islands','Council Area',22870),('South Ayrshire','Council Area',112140),('South Lanarkshire','Council Area',320820),('Stirling','Council Area',94080),('West Dunbartonshire','Council Area',88340),('West Lothian','Council Area',183820),('NORTHERN IRELAND','Country',1895510),('Antrim and Newtownabbey','Local Government District',143756),('Ards and North Down','Local Government District',162056),('Armagh City, Banbridge and Craigavon','Local Government District',217232),('Belfast','Local Government District',342560),('Causeway Coast and Glens','Local Government District',144943),('Derry City and Strabane','Local Government District',151109),('Fermanagh and Omagh','Local Government District',117337),('Lisburn and Castlereagh','Local Government District',146452),('Mid and East Antrim','Local Government District',139443),('Mid Ulster','Local Government District',148953),('Newry, Mourne and Down','Local Government District',181669),('Northamptonshire','Unitary Authority',757181),('Cornwall and Isles of Scilly','Unitary Authority',575525),('Hackney and City of London','London Borough',291879);
/*!40000 ALTER TABLE `cutdownpopulation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `population2020`
--

DROP TABLE IF EXISTS `population2020`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `population2020` (
  `Area` text,
  `Locality Type` text,
  `Population` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `population2020`
--

LOCK TABLES `population2020` WRITE;
/*!40000 ALTER TABLE `population2020` DISABLE KEYS */;
INSERT INTO `population2020` VALUES ('UNITED KINGDOM','Country',67081234),('GREAT BRITAIN','Country',65185724),('ENGLAND AND WALES','Country',59719724),('ENGLAND','Country',56550138),('NORTH EAST','Region',2680763),('County Durham','Unitary Authority',533149),('Darlington','Unitary Authority',107402),('Hartlepool','Unitary Authority',93836),('Middlesbrough','Unitary Authority',141285),('Northumberland','Unitary Authority',323820),('Redcar and Cleveland','Unitary Authority',137228),('Stockton-on-Tees','Unitary Authority',197419),('Tyne and Wear (Met County)','Metropolitan County',1146624),('Gateshead','Metropolitan District',201950),('Newcastle upon Tyne','Metropolitan District',306824),('North Tyneside','Metropolitan District',208871),('South Tyneside','Metropolitan District',151133),('Sunderland','Metropolitan District',277846),('NORTH WEST','Region',7367456),('Blackburn with Darwen','Unitary Authority',150030),('Blackpool','Unitary Authority',138381),('Cheshire East','Unitary Authority',386667),('Cheshire West and Chester','Unitary Authority',343823),('Halton','Unitary Authority',129759),('Warrington','Unitary Authority',209397),('Cumbria','County',499781),('Allerdale','Non-metropolitan District',97831),('Barrow-in-Furness','Non-metropolitan District',66726),('Carlisle','Non-metropolitan District',108524),('Copeland','Non-metropolitan District',68041),('Eden','Non-metropolitan District',53754),('South Lakeland','Non-metropolitan District',104905),('Greater Manchester (Met County)','Metropolitan County',2848286),('Bolton','Metropolitan District',288248),('Bury','Metropolitan District',190708),('Manchester','Metropolitan District',555741),('Oldham','Metropolitan District',237628),('Rochdale','Metropolitan District',223659),('Salford','Metropolitan District',262697),('Stockport','Metropolitan District',294197),('Tameside','Metropolitan District',227117),('Trafford','Metropolitan District',237579),('Wigan','Metropolitan District',330712),('Lancashire','County',1227076),('Burnley','Non-metropolitan District',89344),('Chorley','Non-metropolitan District',118870),('Fylde','Non-metropolitan District',81211),('Hyndburn','Non-metropolitan District',81133),('Lancaster','Non-metropolitan District',148119),('Pendle','Non-metropolitan District',92145),('Preston','Non-metropolitan District',144147),('Ribble Valley','Non-metropolitan District',62026),('Rossendale','Non-metropolitan District',71432),('South Ribble','Non-metropolitan District',111086),('West Lancashire','Non-metropolitan District',114496),('Wyre','Non-metropolitan District',113067),('Merseyside (Met County)','Metropolitan County',1434256),('Knowsley','Metropolitan District',152452),('Liverpool','Metropolitan District',500474),('Sefton','Metropolitan District',275899),('St. Helens','Metropolitan District',181095),('Wirral','Metropolitan District',324336),('YORKSHIRE AND THE HUMBER','Region',5526350),('East Riding of Yorkshire','Unitary Authority',343201),('Kingston upon Hull, City of','Unitary Authority',259126),('North East Lincolnshire','Unitary Authority',159364),('North Lincolnshire','Unitary Authority',172748),('York','Unitary Authority',211012),('North Yorkshire','County',620610),('Craven','Non-metropolitan District',57338),('Hambleton','Non-metropolitan District',91932),('Harrogate','Non-metropolitan District',161545),('Richmondshire','Non-metropolitan District',53732),('Ryedale','Non-metropolitan District',55629),('Scarborough','Non-metropolitan District',108737),('Selby','Non-metropolitan District',91697),('South Yorkshire (Met County)','Metropolitan County',1415054),('Barnsley','Metropolitan District',248071),('Doncaster','Metropolitan District',312785),('Rotherham','Metropolitan District',264984),('Sheffield','Metropolitan District',589214),('West Yorkshire (Met County)','Metropolitan County',2345235),('Bradford','Metropolitan District',542128),('Calderdale','Metropolitan District',211439),('Kirklees','Metropolitan District',441290),('Leeds','Metropolitan District',798786),('Wakefield','Metropolitan District',351592),('EAST MIDLANDS','Region',4865583),('Derby','Unitary Authority',256814),('Leicester','Unitary Authority',354036),('North NorthamptonshireÂ ','Unitary Authority',350448),('Nottingham','Unitary Authority',337098),('Rutland','Unitary Authority',40476),('West NorthamptonshireÂ ','Unitary Authority',406733),('Derbyshire','County',807183),('Amber Valley','Non-metropolitan District',128829),('Bolsover','Non-metropolitan District',81305),('Chesterfield','Non-metropolitan District',104930),('Derbyshire Dales','Non-metropolitan District',72422),('Erewash','Non-metropolitan District',115332),('High Peak','Non-metropolitan District',92633),('North East Derbyshire','Non-metropolitan District',102216),('South Derbyshire','Non-metropolitan District',109516),('Leicestershire','County',713085),('Blaby','Non-metropolitan District',101950),('Charnwood','Non-metropolitan District',188416),('Harborough','Non-metropolitan District',95537),('Hinckley and Bosworth','Non-metropolitan District',113666),('Melton','Non-metropolitan District',51394),('North West Leicestershire','Non-metropolitan District',104809),('Oadby and Wigston','Non-metropolitan District',57313),('Lincolnshire','County',766333),('Boston','Non-metropolitan District',70837),('East Lindsey','Non-metropolitan District',142030),('Lincoln','Non-metropolitan District',100049),('North Kesteven','Non-metropolitan District',118149),('South Holland','Non-metropolitan District',95857),('South Kesteven','Non-metropolitan District',143225),('West Lindsey','Non-metropolitan District',96186),('Nottinghamshire','County',833377),('Ashfield','Non-metropolitan District',128337),('Bassetlaw','Non-metropolitan District',118280),('Broxtowe','Non-metropolitan District',114627),('Gedling','Non-metropolitan District',118239),('Mansfield','Non-metropolitan District',109351),('Newark and Sherwood','Non-metropolitan District',123127),('Rushcliffe','Non-metropolitan District',121416),('WEST MIDLANDS','Region',5961929),('Herefordshire, County of','Unitary Authority',193615),('Shropshire','Unitary Authority',325415),('Stoke-on-Trent','Unitary Authority',256622),('Telford and Wrekin','Unitary Authority',181322),('Staffordshire','County',883172),('Cannock Chase','Non-metropolitan District',101484),('East Staffordshire','Non-metropolitan District',120923),('Lichfield','Non-metropolitan District',105637),('Newcastle-under-Lyme','Non-metropolitan District',129610),('South Staffordshire','Non-metropolitan District',112369),('Stafford','Non-metropolitan District',137858),('Staffordshire Moorlands','Non-metropolitan District',98427),('Tamworth','Non-metropolitan District',76864),('Warwickshire','County',583786),('North Warwickshire','Non-metropolitan District',65452),('Nuneaton and Bedworth','Non-metropolitan District',130373),('Rugby','Non-metropolitan District',110650),('Stratford-on-Avon','Non-metropolitan District',132402),('Warwick','Non-metropolitan District',144909),('West Midlands (Met County)','Metropolitan County',2939927),('Birmingham','Metropolitan District',1140525),('Coventry','Metropolitan District',379387),('Dudley','Metropolitan District',322363),('Sandwell','Metropolitan District',329042),('Solihull','Metropolitan District',217487),('Walsall','Metropolitan District',286716),('Wolverhampton','Metropolitan District',264407),('Worcestershire','County',598070),('Bromsgrove','Non-metropolitan District',100569),('Malvern Hills','Non-metropolitan District',79445),('Redditch','Non-metropolitan District',85568),('Worcester','Non-metropolitan District',100265),('Wychavon','Non-metropolitan District',131084),('Wyre Forest','Non-metropolitan District',101139),('EAST','Region',6269161),('Bedford','Unitary Authority',174687),('Central Bedfordshire','Unitary Authority',294096),('Luton','Unitary Authority',213528),('Peterborough','Unitary Authority',202626),('Southend-on-Sea','Unitary Authority',182773),('Thurrock','Unitary Authority',175531),('Cambridgeshire','County',657204),('Cambridge','Non-metropolitan District',125063),('East Cambridgeshire','Non-metropolitan District',90172),('Fenland','Non-metropolitan District',102080),('Huntingdonshire','Non-metropolitan District',178985),('South Cambridgeshire','Non-metropolitan District',160904),('Essex','County',1497759),('Basildon','Non-metropolitan District',187558),('Braintree','Non-metropolitan District',153091),('Brentwood','Non-metropolitan District',77242),('Castle Point','Non-metropolitan District',90524),('Chelmsford','Non-metropolitan District',179549),('Colchester','Non-metropolitan District',197200),('Epping Forest','Non-metropolitan District',132175),('Harlow','Non-metropolitan District',87280),('Maldon','Non-metropolitan District',65401),('Rochford','Non-metropolitan District',87627),('Tendring','Non-metropolitan District',147353),('Uttlesford','Non-metropolitan District',92759),('Hertfordshire','County',1195672),('Broxbourne','Non-metropolitan District',97592),('Dacorum','Non-metropolitan District',155457),('East Hertfordshire','Non-metropolitan District',151786),('Hertsmere','Non-metropolitan District',105471),('North Hertfordshire','Non-metropolitan District',133463),('St Albans','Non-metropolitan District',149317),('Stevenage','Non-metropolitan District',88104),('Three Rivers','Non-metropolitan District',93966),('Watford','Non-metropolitan District',96623),('Welwyn Hatfield','Non-metropolitan District',123893),('Norfolk','County',914039),('Breckland','Non-metropolitan District',141255),('Broadland','Non-metropolitan District',131931),('Great Yarmouth','Non-metropolitan District',99198),('King\'s Lynn and West Norfolk','Non-metropolitan District',151245),('North Norfolk','Non-metropolitan District',105167),('Norwich','Non-metropolitan District',142177),('South Norfolk','Non-metropolitan District',143066),('Suffolk','County',761246),('Babergh','Non-metropolitan District',92735),('East Suffolk','Non-metropolitan District',250373),('Ipswich','Non-metropolitan District',135979),('Mid Suffolk','Non-metropolitan District',104857),('West Suffolk','Non-metropolitan District',177302),('LONDON','Region',9002488),('Camden','London Borough',279516),('City of London','London Borough',10938),('Hackney','London Borough',280941),('Hammersmith and Fulham','London Borough',183544),('Haringey','London Borough',266357),('Islington','London Borough',248115),('Kensington and Chelsea','London Borough',156864),('Lambeth','London Borough',321813),('Lewisham','London Borough',305309),('Newham','London Borough',355266),('Southwark','London Borough',320017),('Tower Hamlets','London Borough',331969),('Wandsworth','London Borough',329735),('Westminster','London Borough',269848),('Barking and Dagenham','London Borough',214107),('Barnet','London Borough',399007),('Bexley','London Borough',249301),('Brent','London Borough',327753),('Bromley','London Borough',332752),('Croydon','London Borough',388563),('Ealing','London Borough',340341),('Enfield','London Borough',333587),('Greenwich','London Borough',289034),('Harrow','London Borough',252338),('Havering','London Borough',260651),('Hillingdon','London Borough',309014),('Hounslow','London Borough',271767),('Kingston upon Thames','London Borough',179142),('Merton','London Borough',206453),('Redbridge','London Borough',305658),('Richmond upon Thames','London Borough',198141),('Sutton','London Borough',207707),('Waltham Forest','London Borough',276940),('SOUTH EAST','Region',9217265),('Bracknell Forest','Unitary Authority',124165),('Brighton and Hove','Unitary Authority',291738),('Buckinghamshire','Unitary Authority',547060),('Isle of Wight','Unitary Authority',142296),('Medway','Unitary Authority',279142),('Milton Keynes','Unitary Authority',270203),('Portsmouth','Unitary Authority',214692),('Reading','Unitary Authority',160337),('Slough','Unitary Authority',149577),('Southampton','Unitary Authority',252872),('West Berkshire','Unitary Authority',158465),('Windsor and Maidenhead','Unitary Authority',151273),('Wokingham','Unitary Authority',173945),('East Sussex','County',558852),('Eastbourne','Non-metropolitan District',103324),('Hastings','Non-metropolitan District',92554),('Lewes','Non-metropolitan District',103525),('Rother','Non-metropolitan District',96716),('Wealden','Non-metropolitan District',162733),('Hampshire','County',1389206),('Basingstoke and Deane','Non-metropolitan District',177760),('East Hampshire','Non-metropolitan District',123838),('Eastleigh','Non-metropolitan District',135520),('Fareham','Non-metropolitan District',116338),('Gosport','Non-metropolitan District',84679),('Hart','Non-metropolitan District',97608),('Havant','Non-metropolitan District',126339),('New Forest','Non-metropolitan District',179649),('Rushmoor','Non-metropolitan District',94387),('Test Valley','Non-metropolitan District',127163),('Winchester','Non-metropolitan District',125925),('Kent','County',1589057),('Ashford','Non-metropolitan District',131018),('Canterbury','Non-metropolitan District',166762),('Dartford','Non-metropolitan District',114051),('Dover','Non-metropolitan District',118514),('Folkestone and Hythe','Non-metropolitan District',113320),('Gravesham','Non-metropolitan District',106890),('Maidstone','Non-metropolitan District',173132),('Sevenoaks','Non-metropolitan District',121387),('Swale','Non-metropolitan District',151015),('Thanet','Non-metropolitan District',141458),('Tonbridge and Malling','Non-metropolitan District',132571),('Tunbridge Wells','Non-metropolitan District',118939),('Oxfordshire','County',696880),('Cherwell','Non-metropolitan District',151846),('Oxford','Non-metropolitan District',151584),('South Oxfordshire','Non-metropolitan District',143782),('Vale of White Horse','Non-metropolitan District',137910),('West Oxfordshire','Non-metropolitan District',111758),('Surrey','County',1199870),('Elmbridge','Non-metropolitan District',137215),('Epsom and Ewell','Non-metropolitan District',81003),('Guildford','Non-metropolitan District',150352),('Mole Valley','Non-metropolitan District',87547),('Reigate and Banstead','Non-metropolitan District',149243),('Runnymede','Non-metropolitan District',90327),('Spelthorne','Non-metropolitan District',99873),('Surrey Heath','Non-metropolitan District',89204),('Tandridge','Non-metropolitan District',88542),('Waverley','Non-metropolitan District',126556),('Woking','Non-metropolitan District',100008),('West Sussex','County',867635),('Adur','Non-metropolitan District',64187),('Arun','Non-metropolitan District',161123),('Chichester','Non-metropolitan District',121508),('Crawley','Non-metropolitan District',112474),('Horsham','Non-metropolitan District',145474),('Mid Sussex','Non-metropolitan District',152142),('Worthing','Non-metropolitan District',110727),('SOUTH WEST','Region',5659143),('Bath and North East Somerset','Unitary Authority',196357),('Bournemouth, Christchurch and Poole','Unitary Authority',396989),('Bristol, City of','Unitary Authority',465866),('Cornwall','Unitary Authority',573299),('Dorset','Unitary Authority',379791),('Isles of Scilly','Unitary Authority',2226),('North Somerset','Unitary Authority',215574),('Plymouth','Unitary Authority',262839),('South Gloucestershire','Unitary Authority',287816),('Swindon','Unitary Authority',222881),('Torbay','Unitary Authority',136218),('Wiltshire','Unitary Authority',504070),('Devon','County',810716),('East Devon','Non-metropolitan District',148080),('Exeter','Non-metropolitan District',133333),('Mid Devon','Non-metropolitan District',83290),('North Devon','Non-metropolitan District',98170),('South Hams','Non-metropolitan District',87946),('Teignbridge','Non-metropolitan District',135039),('Torridge','Non-metropolitan District',68719),('West Devon','Non-metropolitan District',56139),('Gloucestershire','County',640650),('Cheltenham','Non-metropolitan District',116043),('Cotswold','Non-metropolitan District',90264),('Forest of Dean','Non-metropolitan District',87107),('Gloucester','Non-metropolitan District',129709),('Stroud','Non-metropolitan District',120903),('Tewkesbury','Non-metropolitan District',96624),('Somerset','County',563851),('Mendip','Non-metropolitan District',116288),('Sedgemoor','Non-metropolitan District',123446),('Somerset West and Taunton','Non-metropolitan District',155421),('South Somerset','Non-metropolitan District',168696),('WALES','Country',3169586),('Isle of Anglesey','Unitary Authority',70440),('Gwynedd','Unitary Authority',125171),('Conwy','Unitary Authority',118184),('Denbighshire','Unitary Authority',96664),('Flintshire','Unitary Authority',156847),('Wrexham','Unitary Authority',136055),('Powys','Unitary Authority',133030),('Ceredigion','Unitary Authority',72895),('Pembrokeshire','Unitary Authority',126751),('Carmarthenshire','Unitary Authority',190073),('Swansea','Unitary Authority',246563),('Neath Port Talbot','Unitary Authority',144386),('Bridgend','Unitary Authority',147539),('Vale of Glamorgan','Unitary Authority',135295),('Cardiff','Unitary Authority',369202),('Rhondda Cynon Taf','Unitary Authority',241873),('Merthyr Tydfil','Unitary Authority',60424),('Caerphilly','Unitary Authority',181731),('Blaenau Gwent','Unitary Authority',70020),('Torfaen','Unitary Authority',94832),('Monmouthshire','Unitary Authority',95164),('Newport','Unitary Authority',156447),('SCOTLAND','Country',5466000),('Aberdeen City','Council Area',229060),('Aberdeenshire','Council Area',260780),('Angus','Council Area',115820),('Argyll and Bute','Council Area',85430),('City of Edinburgh','Council Area',527620),('Clackmannanshire','Council Area',51290),('Dumfries and Galloway','Council Area',148290),('Dundee City','Council Area',148820),('East Ayrshire','Council Area',121600),('East Dunbartonshire','Council Area',108750),('East Lothian','Council Area',107900),('East Renfrewshire','Council Area',96060),('Falkirk','Council Area',160560),('Fife','Council Area',374130),('Glasgow City','Council Area',635640),('Highland','Council Area',235430),('Inverclyde','Council Area',77060),('Midlothian','Council Area',93150),('Moray','Council Area',95710),('Na h-Eileanan Siar','Council Area',26500),('North Ayrshire','Council Area',134250),('North Lanarkshire','Council Area',341140),('Orkney Islands','Council Area',22400),('Perth and Kinross','Council Area',151910),('Renfrewshire','Council Area',179390),('Scottish Borders','Council Area',115240),('Shetland Islands','Council Area',22870),('South Ayrshire','Council Area',112140),('South Lanarkshire','Council Area',320820),('Stirling','Council Area',94080),('West Dunbartonshire','Council Area',88340),('West Lothian','Council Area',183820),('NORTHERN IRELAND','Country',1895510),('Antrim and Newtownabbey','Local Government District',143756),('Ards and North Down','Local Government District',162056),('Armagh City, Banbridge and Craigavon','Local Government District',217232),('Belfast','Local Government District',342560),('Causeway Coast and Glens','Local Government District',144943),('Derry City and Strabane','Local Government District',151109),('Fermanagh and Omagh','Local Government District',117337),('Lisburn and Castlereagh','Local Government District',146452),('Mid and East Antrim','Local Government District',139443),('Mid Ulster','Local Government District',148953),('Newry, Mourne and Down','Local Government District',181669);
/*!40000 ALTER TABLE `population2020` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` binary(150) NOT NULL,
  `last_area` varchar(50) DEFAULT NULL,
  `last_rate` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES ('Lilly',_binary '112651476888739100\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL),('LillyPoole',_binary '14e8b4f6834e8a7812183d2ad9dd8c17\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL),('LlouisePoole4',_binary 'a64eb7c6abe8010318b2f15cd7178699\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL),('LouisePoole',_binary '183a2bfef96af7fa66b9a97645f243c6\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL),('LouisePoole1',_binary 'a64eb7c6abe8010318b2f15cd7178699\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL),('LouisePoole2',_binary 'a64eb7c6abe8010318b2f15cd7178699\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL),('LouisePoole3',_binary 'a64eb7c6abe8010318b2f15cd7178699\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL),('LouisePoole4',_binary 'a64eb7c6abe8010318b2f15cd7178699\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL);
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-03 12:45:07
