begin
    Facter.serialnumber
rescue
    facter.loadfacts()
end
Facter.add("hostidentity") do
    setcode do
        identity = nil
        begin
            identity_file = "/etc/hostidentity"
            identity = File.open(identity_file) { |f| f.readline
} if File.exists?(identity_file)
            unless identity
                identity = Facter.value('serialnumber') if Facter.value('virtual') != "xenu"
            end
            unless identity
                identity = Facter::Util::Resolution.exec("ssh-keygen -lf /etc/ssh/ssh_host_rsa_key | awk '{print $2}' | sed -e 's/://g'")
                identity = "badidentity-" + identity if identity
            end
        rescue Exception
        end
        identity.to_s.strip
    end
end
