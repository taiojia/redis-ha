#!/usr/bin/env python

import os
import subprocess

class noflib:  
    def execute_get_output(self, *command):
        """Execute and return stdout."""
        self.devnull = open(os.devnull, 'w')
        self.command = map(str, command)
        self.proc = subprocess.Popen(self.command, close_fds=True, stdout=subprocess.PIPE, stderr=self.devnull)
        self.devnull.close()
        self.stdout = self.proc.communicate()[0]
        return self.stdout.strip()

    def execute(self, *command):
        """Execute without returning stdout."""
        self.devnull = open(os.devnull, 'w')
        self.command = map(str, command)
        subprocess.call(self.command, close_fds=True, stdout=self.devnull, stderr=self.devnull)
        self.devnull.close()