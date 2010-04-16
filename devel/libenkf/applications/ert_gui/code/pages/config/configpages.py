from widgets.configpanel import ConfigPanel
import eclipse
import analysis
import queuesystem
import systemenv
import plot
import ensemble
import observations
import simulations
import dbase
import action
import log

class ConfigPages(ConfigPanel):
    def __init__(self, parent):
        ConfigPanel.__init__(self, parent)

        eclipse.createEclipsePage(self, parent)
        analysis.createAnalysisPage(self, parent)
        queuesystem.createQueueSystemPage(self, parent)
        systemenv.createSystemPage(self, parent)
        plot.createPlotPage(self, parent)
        ensemble.createEnsemblePage(self, parent)
        observations.createObservationsPage(self, parent)
        simulations.createSimulationsPage(self, parent)
        dbase.createDbasePage(self, parent)
        action.createActionPage(self, parent)
        log.createLogPage(self, parent)