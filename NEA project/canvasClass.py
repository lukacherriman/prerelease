class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=4, height=4):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=100)
        super().__init__(fig)
        self.setParent(parent)
        self.parent = parent

    def plot_graph(self, x, y, x_label, y_label, chart_title):
        # plots line graphs with a single line, and the map graph with no tick labels
        self.line1 = self.ax.plot(x, y)

        if x_label != "":
            self.ax.set(xlabel=x_label, ylabel=y_label, title=chart_title)
            self.ax.grid()
        else:
            self.ax.set_yticklabels([])
            self.ax.set_xticklabels([])
            self.ax.axis('equal')
            sides = [self.ax.spines["right"], self.ax.spines["left"], self.ax.spines["top"], self.ax.spines["bottom"]]
            for side in sides:
                side.set_visible(False)
            plt.tight_layout()

    def plot_dual_graph(self, x1, y1, x2, y2, line1, line2, x_label, y_label, chart_title):
        # plots a graph wih 2 lines
        self.line1 = self.ax.plot(x1, y1, label=line1)
        self.line2 = self.ax.plot(x2, y2, label=line2)
        self.ax.set(xlabel=x_label, ylabel=y_label, title=chart_title)
        self.ax.grid()
        self.ax.legend()

    def plot_triple_graph(self, x, y1, y2, y3, line1, line2, line3, x_label, y_label, chart_title):
        # plots a graph with 3 lines for progress chart
        self.ax.plot(x, y1, label=line1)
        self.ax.plot(x, y2, label=line2)
        self.ax.plot(x, y3, label=line3)
        self.ax.set(xlabel=x_label, ylabel=y_label, title=chart_title)
        self.ax.grid()
        self.ax.legend()

    def plot_scatter(self, x, y, x_label, y_label, chart_title):
        # plots scatter graph for power v hr
        self.ax.scatter(x, y)
        self.ax.grid()
        self.ax.set(xlabel=x_label, ylabel=y_label, title=chart_title)

    def plot_overlap_graph(self, longitude, latitude, time, time_interval=600):
        # plots the compare segments graph, plots a line for each segment after making segments
        plt.tight_layout()
        plot_points = [[], [], []]
        self.parent.segments = []
        self.ax.axis('equal')
        for i in range(len(time)-1):
            plot_points[0].append(longitude[i])
            plot_points[1].append(latitude[i])
            plot_points[2].append(time[i])
            if time[i] > plot_points[2][0] + time_interval or longitude[i] > longitude[i+1] + 0.001 or longitude[i] < longitude[i+1] - 0.001\
                    or latitude[i] > latitude[i+1] + 0.001 or latitude[i] < latitude[i+1] - 0.001 or time[i] < plot_points[2][0] - time_interval:
                self.ax.plot(plot_points[0], plot_points[1])
                self.parent.segments.append(plot_points)
                plot_points = [[], [], []]
        plt.yticks(color="#FFFFFF")
        plt.xticks(color="#FFFFFF")
        sides = [self.ax.spines["right"], self.ax.spines["left"], self.ax.spines["top"], self.ax.spines["bottom"]]
        for side in sides:
            side.set_visible(False)

    def clear(self):
        self.ax.lines[0].remove()
