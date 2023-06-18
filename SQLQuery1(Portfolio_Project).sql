SELECT *
FROM Portfolio_project..CovidDeaths
WHERE continent is not null
ORDER BY 3,4

--SELECT *
--FROM Portfolio_project..CovidVaccinations
--ORDER BY 3,4

--Select Data
SELECT Location, date, total_cases, new_cases, total_deaths, population
FROM Portfolio_project..CovidDeaths
ORDER BY 1,2

-- Total Cases vs Total Deaths
SELECT Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS DeathPercentage
FROM Portfolio_project..CovidDeaths
WHERE location = 'Malaysia'
ORDER BY 1,2

-- Total Cases vs Population
-- Percentage population got covid
SELECT Location, date, total_cases, Population, (total_deaths/population)*100 AS DeathPercentage
FROM Portfolio_project..CovidDeaths
WHERE location like '%Malaysia%'
ORDER BY 1,2

--Highest Country infection rate compared to population
SELECT Location, population, MAX(total_cases) as HighestInfectionCount, MAX(total_deaths/population)*100 AS PercentPopulationInfected
FROM Portfolio_project..CovidDeaths
--WHERE location like '%Malaysia%'
GROUP BY location, population
ORDER BY PercentPopulationInfected DESC

-- Countries with Highest Death Count per Population
SELECT Location, MAX(cast(Total_deaths as int)) as TotalDeathCount
FROM Portfolio_project..CovidDeaths
WHERE continent is not null
GROUP BY location
ORDER BY TotalDeathCount DESC

-- group by continent
SELECT continent, MAX(cast(Total_deaths as int)) as TotalDeathCount
FROM Portfolio_project..CovidDeaths
WHERE continent is not null
GROUP BY continent
ORDER BY TotalDeathCount DESC

-- continent with the highest death count per population
SELECT continent, MAX(cast(Total_deaths as int)) as TotalDeathCount
FROM Portfolio_project..CovidDeaths
WHERE continent is not null
GROUP BY continent
ORDER BY TotalDeathCount DESC

-- global numbers
SELECT SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 AS DeathPercentage
FROM Portfolio_project..CovidDeaths
--WHERE location like '%Malaysia%'
WHERE continent is not null
--GROUP BY date
ORDER BY 1,2

-- joining table
-- total population vs vaccinations
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
FROM Portfolio_project..CovidDeaths dea
JOIN Portfolio_project..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
ORDER BY 2,3

-- CTE
WITH PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
AS
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(CONVERT(int,vac.new_vaccinations)) OVER(PARTITION BY dea.location ORDER BY dea.location, dea.Date) as RollingPeopleVaccinated
--(RollingPeopleVaccinated/population)*100
FROM Portfolio_project..CovidDeaths dea
JOIN Portfolio_project..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
--ORDER BY 2,3
)
SELECT *, (RollingPeopleVaccinated/Population)*100
FROM PopvsVac

-- TEMP TABLE
DROP TABLE if exists #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

INSERT INTO #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(CONVERT(int,vac.new_vaccinations)) OVER(PARTITION BY dea.location ORDER BY dea.location, dea.Date) as RollingPeopleVaccinated
--(RollingPeopleVaccinated/population)*100
FROM Portfolio_project..CovidDeaths dea
JOIN Portfolio_project..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
--ORDER BY 2,3

SELECT *, (RollingPeopleVaccinated/Population)*100
FROM #PercentPopulationVaccinated


-- Create view to store data for visualization
CREATE VIEW PercentPopulationVaccinated AS
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(CONVERT(int,vac.new_vaccinations)) OVER(PARTITION BY dea.location ORDER BY dea.location, dea.Date) as RollingPeopleVaccinated
--(RollingPeopleVaccinated/population)*100
FROM Portfolio_project..CovidDeaths dea
JOIN Portfolio_project..CovidVaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
--ORDER BY 2,3


SELECT *
FROM PercentPopulationVaccinated


