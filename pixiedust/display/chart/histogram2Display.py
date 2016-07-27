# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2016
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from .display import ChartDisplay
import matplotlib.pyplot as plt
import numpy as np
    
class Histogram2Display(Mpld3ChartDisplay):
    
    def doRenderMpld3(self, handlerId, fig, ax, colormap, keyFields, keyFieldValues, keyFieldLabels, valueFields, valueFieldValues):
        numColumns = len(keyFieldValues)
        for i, valueField in enumerate(valueFields):
            xs = keyFieldValues
            ys = valueFieldValues[i]
            plt.hist(x, 30, histtype='bar', fc='lightblue', alpha=0.5);
        plt.xticks(np.arange(numColumns),keyFieldLabels)
        plt.xlabel(", ".join(keyFields), fontsize=18)
        